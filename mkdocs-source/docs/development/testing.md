# Testing Guide

Comprehensive testing strategy and guidelines for DinoDB.

## Testing Framework

### Swift Testing Framework
DinoDB uses the modern Swift Testing framework (Swift 6 compatible):
- **Structured Testing**: Clear test organization
- **Async Support**: Built-in async/await testing
- **Parameterized Tests**: Data-driven testing
- **Custom Expectations**: Tailored assertions

### Testing Philosophy
- **Test-Driven Development**: Write tests before implementation
- **90% Coverage Target**: Comprehensive test coverage
- **Fast Feedback**: Quick test execution
- **Reliable Tests**: Deterministic and stable

## Test Structure

### Directory Organization
```
DinoDBTests/
├── Unit/
│   ├── Models/
│   ├── Managers/
│   └── Utilities/
├── Integration/
│   ├── AWS/
│   └── DataFlow/
└── UI/
    ├── Views/
    └── Workflows/
```

### Test Categories

#### Unit Tests
- **Models**: SwiftData model validation
- **Managers**: Business logic testing
- **Utilities**: Helper function testing
- **ViewModels**: State management testing

#### Integration Tests
- **AWS Integration**: DynamoDB operations
- **Data Flow**: End-to-end scenarios
- **Authentication**: Credential management
- **Performance**: Load and timing tests

#### UI Tests
- **User Workflows**: Complete user scenarios
- **Navigation**: View transitions
- **Forms**: Input validation
- **Accessibility**: Screen reader support

## Running Tests

### Command Line
```bash
# Run all tests
xcodebuild test -project DinoDB.xcodeproj -scheme DinoDB

# Run only unit tests
xcodebuild test -project DinoDB.xcodeproj -scheme DinoDB -only-testing:DinoDBTests

# Run with code coverage
xcodebuild test -project DinoDB.xcodeproj -scheme DinoDB -enableCodeCoverage YES

# Run specific test class
xcodebuild test -project DinoDB.xcodeproj -scheme DinoDB -only-testing:DinoDBTests/AccountModelTests
```

### Xcode Integration
- **Test Navigator**: Visual test management
- **Test Reports**: Detailed results and coverage
- **Debugging**: Breakpoints in tests
- **Performance Testing**: XCTMetric integration

## Test Coverage

### Current Coverage
- ✅ **KeychainHelper**: 95% coverage
- ✅ **Account Model**: 90% coverage  
- ✅ **DynamoDBManager**: 85% coverage
- 🔄 **CloudWatchManager**: 70% coverage (in progress)
- ⏳ **UI Components**: 60% coverage (planned)

### Coverage Requirements
- **New Code**: 90% minimum coverage
- **Critical Paths**: 100% coverage
- **Security Code**: 100% coverage
- **Error Handling**: 95% coverage

### Coverage Tools
```bash
# Generate coverage report
xcodebuild test -project DinoDB.xcodeproj -scheme DinoDB \
  -enableCodeCoverage YES \
  -resultBundlePath TestResults.xcresult

# View coverage in Xcode
open TestResults.xcresult
```

## Testing Patterns

### Unit Test Example
```swift
import Testing
@testable import DinoDB

struct AccountModelTests {
    @Test func testAccountCreation() async throws {
        // Given
        let account = Account(
            name: "Test Account",
            accessKeyId: "AKIATEST",
            region: "us-east-1"
        )
        
        // When
        let isValid = account.isValid
        
        // Then
        #expect(isValid == true)
        #expect(account.name == "Test Account")
    }
    
    @Test func testAccountValidation() async throws {
        // Given
        let invalidAccount = Account(name: "", accessKeyId: "", region: "")
        
        // When/Then
        #expect(invalidAccount.isValid == false)
    }
}
```

### Integration Test Example
```swift
struct DynamoDBManagerTests {
    @Test func testListTables() async throws {
        // Given
        let mockCredentials = AWSCredentials(accessKey: "test", secretKey: "test")
        let manager = DynamoDBManager()
        
        // When
        let tables = try await manager.listTables(credentials: mockCredentials)
        
        // Then
        #expect(tables.count >= 0)
    }
}
```

### UI Test Example
```swift
import XCTest

final class DinoDBUITests: XCTestCase {
    func testAccountListNavigation() throws {
        let app = XCUIApplication()
        app.launch()
        
        // Test account list appears
        XCTAssertTrue(app.staticTexts["Accounts"].exists)
        
        // Test add account button
        app.buttons["Add Account"].tap()
        XCTAssertTrue(app.navigationBars["Add Account"].exists)
    }
}
```

## Mocking and Test Doubles

### AWS Service Mocking
```swift
protocol DynamoDBClientProtocol {
    func listTables() async throws -> [String]
}

class MockDynamoDBClient: DynamoDBClientProtocol {
    var mockTables: [String] = []
    var shouldThrowError = false
    
    func listTables() async throws -> [String] {
        if shouldThrowError {
            throw AWSError.unauthorized
        }
        return mockTables
    }
}
```

### SwiftData Mocking
```swift
@MainActor
class TestModelContainer {
    static let shared: ModelContainer = {
        let schema = Schema([Account.self])
        let config = ModelConfiguration(isStoredInMemoryOnly: true)
        return try! ModelContainer(for: schema, configurations: [config])
    }()
}
```

## Performance Testing

### Metrics Collection
```swift
@Test func testTableLoadPerformance() async throws {
    let startTime = CFAbsoluteTimeGetCurrent()
    
    // Perform operation
    let tables = try await dynamoDBManager.listTables()
    
    let timeElapsed = CFAbsoluteTimeGetCurrent() - startTime
    #expect(timeElapsed < 2.0) // Should complete within 2 seconds
}
```

### Memory Testing
```swift
@Test func testMemoryUsage() async throws {
    let initialMemory = getMemoryUsage()
    
    // Perform memory-intensive operation
    try await loadLargeDataset()
    
    // Force garbage collection
    autoreleasepool {}
    
    let finalMemory = getMemoryUsage()
    #expect(finalMemory - initialMemory < 50_000_000) // 50MB limit
}
```

## Test Data Management

### Test Fixtures
```swift
struct TestData {
    static let sampleAccount = Account(
        name: "Test Account",
        accessKeyId: "AKIATEST123",
        region: "us-east-1"
    )
    
    static let sampleTables = ["Users", "Products", "Orders"]
    
    static let sampleItem: [String: Any] = [
        "id": "123",
        "name": "Test Item",
        "created": Date()
    ]
}
```

### Database Seeding
```swift
@MainActor
class DatabaseSeeder {
    static func seedTestData(context: ModelContext) {
        let accounts = [
            TestData.sampleAccount,
            Account(name: "Prod Account", accessKeyId: "AKIAPROD", region: "us-west-2")
        ]
        
        accounts.forEach { context.insert($0) }
        try! context.save()
    }
}
```

## Continuous Integration

### GitHub Actions
```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          xcodebuild test \
            -project DinoDB.xcodeproj \
            -scheme DinoDB \
            -enableCodeCoverage YES
```

### Quality Gates
- All tests must pass
- Code coverage >90% for new code
- Performance benchmarks met
- No memory leaks detected
- Security tests pass

## Debugging Tests

### Common Issues
- **Async Test Failures**: Use proper async/await patterns
- **UI Test Flakiness**: Add explicit waits
- **Memory Leaks**: Check retain cycles
- **Mock Setup**: Verify mock configurations

### Debug Tools
- **Test Logs**: Detailed test execution logs
- **Memory Graph**: Visual memory analysis
- **Time Profiler**: Performance bottleneck identification
- **Network Profiler**: API call analysis

*This is a stub - full documentation will be generated from project source*