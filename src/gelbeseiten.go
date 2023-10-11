package main

import (
	"fmt"
	"strings"

	"github.com/gocolly/colly"
)

func GelbeSeiten() {
	// Instantiate default collector
	c := colly.NewCollector(
		// Visit only domains: gelbeseiten.de
		//colly.AllowedDomains("gelbeseiten.de"),
		colly.UserAgent("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"),
	)

	//links := []string{}

	// On every a element which has href attribute call callback
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		link := e.Attr("href")
		// Print link
		// fmt.Printf("Link found: %q -> %s\n", e.Text, link)
		// Visit link found on page
		// Only those links are visited which are in AllowedDomains
		//c.Visit(e.Request.AbsoluteURL(link))

		if strings.Contains(link, "gsbiz") {
			fmt.Printf("Link found: -> %s\n", link)
			c.Visit(e.Request.AbsoluteURL(link))
			c.OnHTML("#content > div > div > div.container.container--relative > section:nth-child(1) > div", func(e *colly.HTMLElement) {
				fmt.Println(e.ChildText(".mod-TeilnehmerKopf__name"))
				fmt.Println(e.ChildText(".mod-TeilnehmerKopf__adresse-daten"))
				fmt.Println(e.ChildText(".mod-TeilnehmerKopf__adresse-daten--noborder"))
			})
		}
	})

	// Before making a request print "Visiting ..."
	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL.String())
	})

	// Start scraping on https://www.gelbeseiten.de
	what := "krankenhaus"
	city := "frankfurt"
	c.Visit(fmt.Sprintf("https://www.gelbeseiten.de/suche/%s/%s?umkreis=4000", what, city))
}
