package main

import (
	_ "github.com/go-sql-driver/mysql"
	"net/http"
	"github.com/labstack/echo"
	"github.com/labstack/echo/middleware"
	"database/sql"
)

type (
	Info struct {
		Tid         int    `json:"tid"`
		Nowtime     string `json:"nowtime"`
		Temperature int8   `json:"temperature"`
		Humidity    uint8  `json:"humidity"`
	}
)

type Infoes struct {
	Code   int    `json:"code"`
	Msg    string `json:"msg"`
	Count  int    `json:"count"`
	Infoes []Info `json:"data"`
}

func main() {
	e := echo.New()
	e.Use(middleware.Recover())
	e.GET("/", index)
	e.GET("/info", info)
	e.Static("/lib", "web/lib")
	e.File("/web", "./web/index.html")
	e.Use(middleware.Logger())
	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins: []string{"*"},
		AllowHeaders: []string{echo.HeaderOrigin, echo.HeaderContentType, echo.HeaderAccept},
	}))
	e.Logger.Fatal(e.Start("127.0.0.1:8000"))
}

func index(c echo.Context) error {
	var hello struct {
		Code    int    `json:"code"`
		Message string `json:"message"`
	}
	hello.Code = 2002
	hello.Message = "Hello World"
	return c.JSON(http.StatusOK, &hello)
}

func info(c echo.Context) error {
	con := DbCon()
	data, err := con.Query("select * from (select tid, nowtime, temperature, humidity from info order by tid desc limit 6) info order by tid")
	if err != nil {
		panic(err)
	}
	defer data.Close()
	defer con.Close()

	result := Infoes{}
	result.Code = 0
	result.Msg = "nil"
	result.Count = 6

	for data.Next() {
		info := Info{}
		err = data.Scan(&info.Tid, &info.Nowtime, &info.Temperature, &info.Humidity)
		if err != nil {
			panic(err)
		}
		result.Infoes = append(result.Infoes, info)
	}
	return c.JSON(http.StatusOK, &result)
}

func DbCon() *sql.DB {
	db, err := sql.Open("mysql", "user:password@tcp(dbhost:3306)/dbname?charset=utf8&timeout=30s")
	if err != nil {
		panic(err)
	}

	err = db.Ping()
	if err != nil {
		panic(err.Error())
	}
	return db
}
