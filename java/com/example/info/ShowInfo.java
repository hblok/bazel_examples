package com.example.info;

public class ShowInfo {

  public static void main(String[] args) {
    InfoProvider.getEnv().stream().sorted().forEach(System.out::println);
  }

}
