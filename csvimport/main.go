package main

import (
	"bytes"
	"encoding/csv"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"io/ioutil"
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
	host  *string
	user  *string
	file  *string
	debug *bool
)

func init() {
	host = flag.String("host", "localhost:", "cayley host:port")
	user = flag.String("user", "", "user id")
	file = flag.String("file", "", "csv file in")
	debug = flag.Bool("debug", false, "debug info")
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

		writeEdge(*host+"/api/v1/write", []edge_t{edge_t{
			// postid -> timelineid
			record[3],
			"isInTimeline",
			record[5],
		}, edge_t{
			// user -> timelineid
			*user,
			"ownTimeline",
			record[5],
		}, edge_t{
			// user <- timelineid
			record[5],
			"ownedByUser",
			*user,
		}})
	}

}

func writeEdge(host string, edges []edge_t) {
	body, err := json.Marshal(edges)
	if err != nil {
		log.Println(err)
	}

	if *debug {
		fmt.Println(string(body))
	}

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

	if *debug {
		b, _ := ioutil.ReadAll(resp.Body)
		var s interface{}
		json.Unmarshal(b, &s)
		fmt.Println(s)
	}
}
