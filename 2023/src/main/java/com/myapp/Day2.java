package com.myapp;

import java.util.List;

public class Day2 {
    public static void main (String [] args) {
        System.out.println("Hello World!");
        part1();
        part2();
    }
    public static void part1() {
        int sum = 0;
        List<String> inputs = Utils.parseInput("day2input1.txt");
        for (int i = 0; i < inputs.size(); i++) {
            String s = inputs.get(i);
            int id = i+1;
            // first part is id, don't care. generate our own since it's incremental
            String gameString = s.split(":")[1].trim();
            String[] games = gameString.split(";");
            int red = 0, green = 0, blue = 0;
            for (String g : games) {
                for (String trial : g.split(",")) {
                    int num = Integer.valueOf(trial.trim().split(" ")[0]);
                    String color = trial.trim().split(" ")[1];
                    switch (color) {
                    case "blue":
                        blue = num;
                        break;
                    case "red":
                        red = num;
                        break;
                    case "green":
                        green = num;
                        break;
                    }
                    if (red > 12 || green > 13 || blue > 14) break;
                }
                if (red > 12 || green > 13 || blue > 14) break;
            }
            if (red > 12 || green > 13 || blue > 14) continue;
            sum += id;
        }
        System.out.println(sum);
    }
    public static void part2() {
        int sum = 0;
//        List<String> inputs = Utils.parseInput("test.txt");
        List<String> inputs = Utils.parseInput("day2input1.txt");
        for (int i = 0; i < inputs.size(); i++) {
            String s = inputs.get(i);
            String gameString = s.split(":")[1].trim();
            String[] games = gameString.split(";");
            int red = 0, green = 0, blue = 0;
            for (String g : games) {
                for (String trial : g.split(",")) {
                    int num = Integer.valueOf(trial.trim().split(" ")[0]);
                    String color = trial.trim().split(" ")[1];
                    switch (color) {
                    case "blue":
                        if (blue < num) blue = num;
                        break;
                    case "red":
                        if (red < num) red = num;
                        break;
                    case "green":
                        if (green < num) green = num;
                        break;
                    }
                }
            }
            int power = red * green * blue;
            sum += power;
        }
        System.out.println(sum);
    }
}
