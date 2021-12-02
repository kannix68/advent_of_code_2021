/**
 * Advent of Code 2021 Day 1 solution.
 * This is currently a fairly minimalistic code.
 */

import java.io.File

val testin = """
199
200
208
210
200
207
240
269
260
263
  """.trimIndent()

/**
 * Get diff of List "as series", first element will be null.
 */
private fun diff(ints: List<Int>): List<Int?> {
  val diffs = ints.mapIndexed { idx, elem -> if (idx == 0) null else elem - ints[idx - 1] }
  return diffs
}

private fun getIncsCount(inp: String): Int {
  //val ints = listOf(1, 2, 3, 2, 1)
  val ints = inp.split("\n").map { it.toInt() };
  val diffs = diff(ints)
  val incs = diffs.filterNotNull().filter { it > 0 }.size
  //println(ints)
  //println(diffs)
  return incs
}

private fun getIncs3Count(inp: String): Int {
  //val ints = listOf(1, 2, 3, 2, 1)
  var ints = inp.split("\n").map{ it.toInt() };
  //println(ints.windowed(3))
  //println(ints.windowed(3).map{it.sum()})
  ints = ints.windowed(3).map{it.sum()}
  val diffs = diff(ints)
  val incs = diffs.filterNotNull().filter{ it > 0 }.size
  //println(ints)
  //println(diffs)
  return incs
}

fun main(args: Array<String>){
  var incs = getIncsCount(testin)
  println("rc=$incs")
  val inp = File("./in/day01.in").readText().trim()
  incs = getIncsCount(inp)
  println("rc=$incs")

  incs = getIncs3Count(testin)
  println("rc=$incs")
  incs = getIncs3Count(inp)
  println("rc=$incs")
}
