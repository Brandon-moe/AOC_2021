from days import *
import unittest
class AdventOfCode2021Tests(unittest.TestCase):
    #DAY 1
    def test_day_1_part_a(self):
        self.assertEqual(day1.solve("test/1.csv",1),7)
    def test_day_1_part_b(self):
        self.assertEqual(day1.solve("test/1.csv",3),5)
    #DAY 2
    def test_day_2_part_a(self):
        self.assertEqual(day2.solve("test/2.csv","a"),150)
    def test_day_2_part_b(self):
        self.assertEqual(day2.solve("test/2.csv","b"),900)
    #DAY 3
    def test_day_3_part_a(self):
        self.assertEqual(day3.solve("test/3.csv",2),198)
    def test_day_3_part_b(self):
        self.assertEqual(day3.solve("test/3.csv",1)*day3.solve("test/3.csv",0),230)
    #DAY 4
    def test_day_4_part_a(self):
        self.assertEqual(day4.solve("test/4.csv")[0],4512)
    def test_day_4_part_b(self):
        self.assertEqual(day4.solve("test/4.csv")[1],1924)
    # #DAY 5
    def test_day_5_part_a(self):
        self.assertEqual(day5.solve("test/5.csv","a"),5)
    def test_day_5_part_b(self):
        self.assertEqual(day5.solve("test/5.csv","b"),12)
    # #DAY 6
    def test_day_6_part_a(self):
        self.assertEqual(day6.solve("test/6.csv",80),5934)
    def test_day_6_part_b(self):
        self.assertEqual(day6.solve("test/6.csv",256),26984457539)
    #DAY 7
    def test_day_7_part_a(self):
        self.assertEqual(day7.solve("test/7.csv")[0],37)
    def test_day_7_part_b(self):
        self.assertEqual(day7.solve("test/7.csv")[1],170)
    #DAY 8
    def test_day_8_part_a(self):
        self.assertEqual(day8.solve("test/8.csv")[0],26)
    def test_day_8_part_b(self):
        self.assertEqual(day8.solve("test/8.csv")[1],61229)
    #DAY 9
    def test_day_9_part_a(self):
        self.assertEqual(day9.solve("test/9.csv")[0],15)
    def test_day_9_part_b(self):
        self.assertEqual(day9.solve("test/9.csv")[1],1134)
    #DAY 10
    def test_day_10_part_a(self):
        self.assertEqual(day10.solve("test/10.csv")[0],26397)
    def test_day_10_part_b(self):
        self.assertEqual(day10.solve("test/10.csv")[1],288957)
    #DAY 11
    def test_day_11_part_a(self):
        self.assertEqual(day11.solve("test/11.csv")[0],1656)
    def test_day_11_part_b(self):
        self.assertEqual(day11.solve("test/11.csv")[1],195)
    #DAY 12
    def test_day_12_part_a(self):
        self.assertEqual(day12.solve("test/12.csv")[0],226)
    def test_day_12_part_b(self):
        self.assertEqual(day12.solve("test/12.csv")[1],3509)
    #DAY 13
    def test_day_13_part_a(self):
        self.assertEqual(day13.solve("test/13.csv",False),17)
    #DAY 14
    def test_day_14_part_a(self):
        self.assertEqual(day14.solve("test/14.csv",10),1588)
    def test_day_14_part_b(self):
        self.assertEqual(day14.solve("test/14.csv",40),2188189693529)
    #DAY 15
    def test_day_15_part_a(self):
        self.assertEqual(day15.solve("test/15.csv","a"),40)
    def test_day_15_part_b(self):
        self.assertEqual(day15.solve("test/15.csv","b"),315)
    #DAY 16
    def test_day_16_part_a(self):
        self.assertEqual(day16.solve("test/16.csv")[0],31)
    def test_day_16_part_b(self):
        self.assertEqual(day16.solve("test/16.csv")[1],54)
    #DAY 17
    def test_day_17_part_a(self):
        self.assertEqual(day17.solve("test/17.csv","a"),45)
    def test_day_17_part_b(self):
        self.assertEqual(day17.solve("test/17.csv","b"),112)
    #DAY 18
    def test_day_18_part_a(self):
        self.assertEqual(day18.solve("test/18.csv")[0],4140)
    def test_day_18_part_b(self):
        self.assertEqual(day18.solve("test/18.csv")[1],3993)
    # #DAY 19
    # def test_day_19_part_a(self):
    #     self.assertEqual(day19.solve("test/19.csv")[0],79)
    # def test_day_19_part_b(self):
    #     self.assertEqual(day19.solve("test/19.csv")[1],3621)
    # #DAY 20
    def test_day_20_part_a(self):
        self.assertEqual(day20.solve("test/20.csv",2),35)
    def test_day_20_part_b(self):
        self.assertEqual(day20.solve("test/20.csv",50),3351)
    # #DAY 21
    def test_day_21_part_a(self):
        self.assertEqual(day21.solve("test/21.csv","a"),739785)
    def test_day_21_part_b(self):
        self.assertEqual(day21.solve("test/21.csv","b"),444356092776315)
    # #DAY 22
    def test_day_22_part_a(self):
        self.assertEqual(day22.solve("test/22a.csv","a"),590784)
    def test_day_22_part_b(self):
        self.assertEqual(day22.solve("test/22b.csv","b"),2758514936282235)
    # #DAY 23
    def test_day_23_part_a(self):
        self.assertEqual(day23.solve("test/23.csv","a"),12521)
    def test_day_23_part_b(self):
        self.assertEqual(day23.solve("test/23.csv","b"),44169)
    # #DAY 24
    def test_day_25_part_a(self):
        self.assertEqual(day25.solve("test/25.csv"),58)

if __name__ == "__main__":
    unittest.main()
