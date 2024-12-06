package com.example.springboot;

import org.springframework.web.bind.annotation.*;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;

@RestController
public class AirlinesController {
	private static String[] airlines = {"AA", "DL", "UA"};

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

	@GetMapping("/airlines")
    @Operation(summary = "Get airlines", description = "Fetch a list of airlines")
    public String getUserById(
            @Parameter(description = "Optional flag - set raise to true to raise an exception")
            @RequestParam(value = "raise", required = false, defaultValue = "false") boolean raise
    ) {
		if (raise) {
			throw new RuntimeException("Exception raised");
		}
		return String.join(", ", airlines);
    }
}
