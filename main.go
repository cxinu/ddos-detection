package main

import (
	// "ddos-detection/alert"
	// "ddos-detection/mitigation"
	"ddos-detection/monitor"
	"log"
	"net/http"
)

func main() {
	go monitor.ResetIPCounts()
	http.HandleFunc("/", monitor.Handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
