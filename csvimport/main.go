package main

import (
	"bytes"
	"encoding/csv"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

type edge_t struct {
	Subject   string `json:"subject"`
	Predicate string `json:"predicate"`
	Object    string `json:"object"`
	// Label interface{} `json:"label"`
}

var (
	host *string
	user *string
	file *string
)

func init() {
	host = flag.String("host", "localhost:", "cayley host:port")
	user = flag.String("user", "", "user id")
	file = flag.String("file", "", "csv file in")
}

func main() {
	flag.Parse()

	csvIn, err := os.Open(*file)
	if err != nil {
		log.Fatal(err)
	}

	csvRd := csv.NewReader(csvIn)
	_, _ = csvRd.Read() // skip first line
	for {
		record, err := csvRd.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}

		// postid <-> timelineid
		writeEdge(*host+"/api/v1/write", edge_t{
			record[3],
			"isIn",
			record[5],
		})

		// user <-> timelineid
		writeEdge(*host+"/api/v1/write", edge_t{
			user,
			"own",
			record[5],
		})
	}

}

func writeEdge(host string, edge edge_t) {
	edges := []edge_t{edge}
	body, err := json.Marshal(edges)
	if err != nil {
		log.Println(err)
	}

	fmt.Println(string(body))
	req, err := http.NewRequest("POST", host, bytes.NewBuffer(body))
	if err != nil {
		log.Println(err)
	}

	req.Header.Set("Content-Type", "application/json")
	client := &http.Client{}

	resp, err := client.Do(req)
	if err != nil {
		log.Println(err)
	}
	defer resp.Body.Close()
}
