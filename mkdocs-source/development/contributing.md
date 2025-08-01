# Contributing

Guidelines for contributing to DinoDB development.

## Getting Started

### Development Setup
1. Fork the repository on GitHub
2. Clone your fork locally
3. Install Xcode 15.0 or later
4. Open `DinoDB.xcodeproj`
5. Build and run the project

### Prerequisites
- macOS 14.0+ for development
- Understanding of SwiftUI and SwiftData
- Familiarity with AWS DynamoDB
- Git workflow knowledge

## Development Guidelines

### Code Style
- Follow Swift API Design Guidelines
- Use SwiftLint for consistent formatting
- Maintain existing architectural patterns
- Write self-documenting code

### Naming Conventions
- **Classes**: PascalCase (e.g., `DynamoDBManager`)
- **Properties**: camelCase (e.g., `tableName`)
- **Constants**: camelCase (e.g., `defaultPageSize`)
- **Enums**: PascalCase cases (e.g., `.loading`, `.loaded`)

### File Organization
- Group related functionality in folders
- Separate views, models, and managers
- Keep files under 500 lines when possible
- Use extensions for protocol conformance

## Mandatory Requirements

### Debug Logging
**ALL code changes MUST include comprehensive debug logging:**

```swift
// Log user actions
DebugLogger.shared.log("User clicked refresh button", category: "UserAction")

// Time AWS operations
let timer = DebugLogger.shared.startTimer()
// ... AWS operation
DebugLogger.shared.endTimer(timer, operation: "ListTables", category: "AWS")

// Log errors with context
DebugLogger.shared.log("Failed to connect: \(error)", category: "Error")
```

### Required Categories
- **UserAction**: All direct user interactions
- **AWS**: DynamoDB and CloudWatch API calls
- **DataOp**: CRUD operations
- **Auth**: Authentication events
- **Performance**: Operations >100ms
- **Error**: All error conditions

### Security Requirements
- ❌ **NEVER log**: AWS credentials, PII, sensitive data
- ✅ **Safe to log**: Account names, table names, counts, errors
- Always use appropriate log categories
- Include context but protect privacy

## Pull Request Process

### Before Submitting
1. **Add comprehensive logging** to all new code
2. Write or update unit tests
3. Run full test suite
4. Update documentation if needed
5. Test debug panel functionality

### PR Checklist
- [ ] Debug logging added with appropriate categories
- [ ] No sensitive data in logs
- [ ] Tests pass with >90% coverage
- [ ] No SwiftLint warnings
- [ ] Documentation updated
- [ ] Debug panel tested

### PR Description Template
```markdown
## Summary
Brief description of changes

## Changes Made
- Detailed list of modifications
- New features or bug fixes
- Performance improvements

## Testing
- Unit tests added/updated
- Manual testing performed
- Debug logging verified

## Debug Logging
- Categories used: UserAction, AWS, DataOp, etc.
- No sensitive data logged
- Debug panel functionality tested
```

## Testing Requirements

### Unit Tests
- **Swift Testing Framework**: Use modern testing patterns
- **90% Coverage**: Target for all new code
- **Mock AWS Services**: Isolated testing
- **Async Testing**: Proper concurrent testing

### Integration Tests
- End-to-end user workflows
- AWS service integration
- Error handling scenarios
- Performance benchmarks

### Manual Testing
- Test in both light and dark themes
- Verify keyboard shortcuts work
- Check accessibility features
- Validate debug panel output

## Code Review Process

### Review Criteria
1. **Logging Compliance**: Comprehensive debug logging
2. **Security**: No credential exposure in logs
3. **Architecture**: Follows MVVM patterns
4. **Performance**: Efficient async operations
5. **Testing**: Adequate test coverage
6. **Documentation**: Clear and accurate

### Reviewer Responsibilities
- Verify debug logging requirements
- Check for security vulnerabilities
- Validate architectural consistency
- Ensure test coverage
- Review documentation updates

## Release Process

### Version Management
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Tag releases in Git
- Update changelog
- Build release notes

### Quality Gates
- All tests must pass
- Code coverage >90%
- No critical security issues
- Performance benchmarks met
- Debug logging verified

## Documentation

### Required Updates
- Update CLAUDE.md for architectural changes
- Add inline code documentation
- Update user-facing documentation
- Include examples and usage patterns

### Documentation Standards
- Clear, concise language
- Code examples with proper syntax highlighting
- Screenshots for UI changes
- Architecture diagrams for complex features

## Community Guidelines

### Communication
- Be respectful and inclusive
- Provide constructive feedback
- Ask questions when unclear
- Share knowledge openly

### Issue Reporting
- Use provided issue templates
- Include reproduction steps
- Provide system information
- Include debug logs (without sensitive data)

### Feature Requests
- Explain the use case clearly
- Consider existing patterns
- Discuss implementation approaches
- Consider maintenance burden

*This is a stub - full documentation will be generated from project source*