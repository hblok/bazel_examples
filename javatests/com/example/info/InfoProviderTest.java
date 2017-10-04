package com.example.info;

import static org.junit.Assert.*;

import java.util.*;

import org.junit.Test;


public class InfoProviderTest {

  @Test
  public void testGetEnv() {
    List<String> env = InfoProvider.getEnv();

    assertTrue(env.size() > 0);
  }
}
