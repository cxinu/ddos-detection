package monitor

import (
	"ddos-detection/alert"
	"ddos-detection/config"
	// "log"
	"net/http"
	"sync"
	"time"
)

var (
	ipRequests = make(map[string]int)
	mu         sync.Mutex
)

func ResetIPCounts() {
	for {
		time.Sleep(1 * time.Minute)
		mu.Lock()
		ipRequests = make(map[string]int)
		mu.Unlock()
	}
}

func Handler(w http.ResponseWriter, r *http.Request) {
	ip := r.RemoteAddr
	mu.Lock()
	ipRequests[ip]++
	count := ipRequests[ip]
	mu.Unlock()

	if count > config.RequestThreshold {
		alert.SendAlert("Potential DDoS detected from IP: " + ip)
	}

	w.Write([]byte("OK"))
}
