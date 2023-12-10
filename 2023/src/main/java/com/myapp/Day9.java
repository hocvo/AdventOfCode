package com.myapp;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.stream.Collectors;

import javafx.util.Pair;

public class Day9
{
    public static void main (String[] args)
    {
        System.out.println("Hello World!");
        List<String> inputs = Utils.parseInput("day9.txt");
//        part1(inputs);
        part2(inputs);
    }

    public static void part1 (List<String> in)
    {
        long start = System.currentTimeMillis();
        long sum = 0;
        for (String s : in) {
            List<Long> nums = Arrays.stream(s.split(" "))
            .mapToLong(l -> Long.parseLong(l)).boxed()
            .collect(Collectors.toList());
            Stack<Long> stack = new Stack<>();
            List<Long> tmp = new ArrayList<>(nums);
            while (!isAllZero(tmp)) {
                List<Long> tmp2 = new ArrayList<>();
                for (int i = 1; i < tmp.size(); i++) {
                    tmp2.add(tmp.get(i) - tmp.get(i-1));
                }
                stack.add(tmp.get(tmp.size()-1));
                tmp = tmp2;
            }
            // pop the 0
            long nextVal = stack.pop();
            while (!stack.isEmpty()) {
                nextVal += stack.pop();
            }
            sum += nextVal;
        }
        long stop = System.currentTimeMillis();
        System.out.println(sum);
        System.out.println((stop-start));
    }
    public static void part2(List<String> in)
    {
        long start = System.currentTimeMillis();
        long sum = 0;
        for (String s : in) {
            List<Long> nums = Arrays.stream(s.split(" "))
            .mapToLong(l -> Long.parseLong(l)).boxed()
            .collect(Collectors.toList());
            Stack<Long> stack = new Stack<>();
            List<Long> tmp = new ArrayList<>(nums);
            while (!isAllZero(tmp)) {
                List<Long> tmp2 = new ArrayList<>();
                for (int i = 1; i < tmp.size(); i++) {
                    tmp2.add(tmp.get(i) - tmp.get(i-1));
                }
                stack.add(tmp.get(0));
                tmp = tmp2;
            }
            // pop the 0
            long nextVal = stack.pop();
            while (!stack.isEmpty()) {
                nextVal = stack.pop() - nextVal;
            }
            sum += nextVal;
        }
        long stop = System.currentTimeMillis();
        System.out.println(sum);
        System.out.println((stop-start));
    }

    public static boolean isAllZero(List<Long> in) {
        if (in.isEmpty()) return false;
        return in.stream().allMatch(l -> l==0);
    }
}
