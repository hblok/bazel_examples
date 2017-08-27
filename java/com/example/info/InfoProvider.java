package com.example.info;

import java.util.*;

public class InfoProvider {

  public static List<String> getEnv() {
    List<String> result = new ArrayList<>();
    
    Map<String, String> env = System.getenv();
    for (String name : env.keySet()) {
      result.add(String.format("%s=%s", name, env.get(name)));
    }

    return result;
  }
}
