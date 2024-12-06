package com.example.springboot;

import io.swagger.v3.oas.annotations.Operation;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @Operation(summary = "Index", description = "No-op hello world")
	@GetMapping("/")
	public String index() {
		return "Greetings from Spring Boot!";
	}

    @Operation(summary = "Health check", description = "Performs a simple health check")
	@GetMapping("/health")
	public String health() {
		return "Health check passed!";
	}
}
