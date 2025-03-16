package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// Constants
const (
	MOD = 1_000_000_007
	PI = 3.14159265358979323846
)
// Fast I/O
var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func main() {
	// Test()
	defer writer.Flush()
	solve()
	// var t int
	// fmt.Fscan(reader, &t)
	// for i := 0; i < t; i++ {
	// 	solve()
	// }
}

// Solve function (Problem logic goes here)
func solve() {
	var n, l int
	fmt.Fscan(reader, &n, &l)
	arr := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &arr[i])
	}
	sort.Strings(arr)
	res := ""
	for _, s:= range arr {
		res += s
	}
	fmt.Fprint(writer, res)
}

// Utility functions

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func binExp(a, b int) int {
	res := 1
	for b > 0 {
		if b%2 == 1 {
			res = (res * a) % MOD
		}
		a = (a * a) % MOD
		b /= 2
	}
	return res
}

func Test() {
    file, err := os.Open("in")
    if err != nil {
        fmt.Fprintln(writer, "Error opening input file:", err)
        return
    }
	reader = bufio.NewReader(file)
}