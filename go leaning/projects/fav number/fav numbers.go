package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("what is your favorite number from 0 thru 10?")
	var fav string
	fmt.Scan(&fav)

	if fav == "0" {
		fmt.Println("Bro, seriously..")
		time.Sleep(time.Second)
		fmt.Println("Zero is nothing, but so are you so at least it balance...")
		time.Sleep(time.Second)

	} else if fav == "1" {
		fmt.Println("One? You deceive me.")
		time.Sleep(time.Second)
		fmt.Println("I guess you like numbers that match your ratings out of 10.")
		time.Sleep(time.Second)

	} else if fav == "2" {
		fmt.Println("Two is an okay favorite")
		time.Sleep(time.Second)
		fmt.Println("For an okay person, and even saying okay feel generous")
		time.Sleep(time.Second)

	} else if fav == "3" {
		fmt.Println("Three, its ironically in the top...")
		time.Sleep(time.Second)
		fmt.Println("Three. If you didn't get it, you need help")
		time.Sleep(time.Second)

	} else if fav == "4" {
		fmt.Println("Four?")
		time.Sleep(time.Second)
		fmt.Println("It didn't occur to me that you were rather autistic...")
		time.Sleep(time.Second)

	} else if fav == "5" {
		fmt.Println("Five?")
		time.Sleep(time.Second)
		fmt.Println("SO predictive. Are you a bot?")
		time.Sleep(time.Second)

	} else if fav == "6" {
		fmt.Println("Six.")
		time.Sleep(time.Second)
		fmt.Println("Were you thinking about 69, you filthy dog?!?")
		time.Sleep(time.Second)

	} else if fav == "7" {
		fmt.Println("Seven!")
		time.Sleep(time.Second)
		fmt.Println("FINALLY, SOMEONE WITH TASTE!!!")
		time.Sleep(time.Second)

	} else if fav == "8" {
		fmt.Println("Eight")
		time.Sleep(time.Second)
		fmt.Println("The second to best choice. You were so close to be a good boy.")
		time.Sleep(time.Second)

	} else if fav == "9" {
		fmt.Println("Nine?")
		time.Sleep(time.Second)
		fmt.Println("But... seven eight nine, so how can you choose it???")
		time.Sleep(time.Second)

	} else {
		fmt.Println("HOW HARD CAN IT BE TO CHOOSE A NUMBER BETWEEN ZERO AND NINE???")
		time.Sleep(time.Second)
		fmt.Println("JUST FUCKING WRITE A NUMBER... 1234567890")
		time.Sleep(time.Second)
		fmt.Println("SEE, IT'S NOT THAT FUCKING HARD")
		time.Sleep(time.Second)
		time.Sleep(time.Second)
	}
}
