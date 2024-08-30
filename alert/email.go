package alert

import (
	"ddos-detection/config"
	"log"
	"net/smtp"
)

func SendAlert(message string) {
	auth := smtp.PlainAuth("", config.SMTPUser, config.SMTPPassword, "smtp.example.com")
	msg := []byte("Subject: DDoS Alert!\n\n" + message)
	err := smtp.SendMail(config.SMTPServer, auth, config.SMTPUser, []string{config.EmailRecipient}, msg)
	if err != nil {
		log.Printf("Failed to send email: %v", err)
	}
}
