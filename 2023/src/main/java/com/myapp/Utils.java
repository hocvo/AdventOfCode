package com.myapp;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

import javafx.util.Pair;

public class Utils {
    public static List<String> parseInput(String filename) {
        Path path = Paths.get("src/main/resources/" + filename);
        try {
            List<String> lines = Files.readAllLines(path, StandardCharsets.UTF_8);
            return lines;
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        return new ArrayList<>();
    }
    
    public static List<Pair<Integer,Integer>> getAdjecentToSymbolIndex(char[][]a, Pair<Integer,Integer> index, boolean includeDiagonal) {
        int[] neighborIndex = {-1,0,1};
        List<Pair<Integer,Integer>> result = new ArrayList<>();
        int r = index.getKey();
        int c = index.getValue();
        for (int rNeighbor : neighborIndex) {
            for (int cNeighbor : neighborIndex) {
                if (!includeDiagonal && rNeighbor+cNeighbor != 1) continue; // up, down, left, right neighbor indices always add up to 1. 
                if (r == rNeighbor && c == cNeighbor) continue;
                Pair<Integer,Integer> neighbor = new Pair<>(r + rNeighbor, c + cNeighbor);
                result.add(neighbor);
            }
        }
        return result;
    }
}
