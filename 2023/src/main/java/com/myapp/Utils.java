package com.myapp;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Utils {
    public static List<String> parseInput(String filename) {
//        ClassLoader classloader = Thread.currentThread().getContextClassLoader();
//        InputStream is = classloader.getResourceAsStream(filename);
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
}
