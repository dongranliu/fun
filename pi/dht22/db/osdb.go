package main

import (
	"github.com/aliyun/aliyun-oss-go-sdk/oss"
	"os"
	"fmt"
	"time"
)

var (
	localfilename  string
	originfilename string
)

const (
	ACCESSKEYID     string = ""
	ACCESSKEYSECRET string = ""
	ENDPOINT        string = ""
	BUCKETNAME      string = ""
)

func main() {
	client, err := oss.New(ENDPOINT, ACCESSKEYID, ACCESSKEYSECRET)
	if err != nil {
		panic(err)
		os.Exit(-1)
	}

	bucket, err := client.Bucket(BUCKETNAME)
	if err != nil {
		panic(err)
		os.Exit(-1)
	}

	t := time.Now().Format("200601021504")
	localfilename = "/home/pi/te/db/" + "te" + "-" + t + "." + "sql"
	originfilename = "tedb/" + "te" + "-" + t + "." + "sql"
	err = bucket.PutObjectFromFile(originfilename, localfilename)
	if err != nil {
		fmt.Println("Error", err)
		os.Exit(-1)
	} else {
		fmt.Println("put success")
	}
}
