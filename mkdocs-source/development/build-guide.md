# Build Guide

Complete guide to building DinoDB from source.

## Prerequisites

### Development Environment
- **Xcode**: 15.0 or later
- **macOS**: 14.0 (Sonoma) or later for development
- **Swift**: 5.9 or later
- **Git**: For source control

### Required SDKs
- AWS SDK for Swift v1.0+
- SwiftUI and SwiftData frameworks
- CloudWatch SDK components

## Quick Start

### Clone Repository
```bash
git clone https://github.com/vegasq/dinodbapp.git
cd dinodbapp
```

### Standard Build
```bash
xcodebuild -project DinoDB.xcodeproj -scheme DinoDB -configuration Debug build
```

### Clean Build
```bash
xcodebuild -project DinoDB.xcodeproj -scheme DinoDB clean build
```

## Build Configurations

### Debug Configuration
- Full debugging symbols
- Debug logging enabled
- Development provisioning
- Faster compilation

### Release Configuration
- Optimized performance
- Reduced binary size
- Distribution provisioning
- Production-ready build

## Project Structure

### Core Directories
```
DinoDB/
├── Models/           # SwiftData models
├── Views/           # SwiftUI views
├── Managers/        # Business logic
├── Documentation/   # Technical docs
└── Tests/          # Unit and UI tests
```

### Key Files
- `DinoDBApp.swift`: Application entry point
- `ContentView.swift`: Main navigation interface
- `DynamoDBManager.swift`: AWS integration
- `Account.swift`: Core data model

## Dependencies

### AWS SDK for Swift
- DynamoDB client integration
- CloudWatch metrics support
- Automatic dependency resolution
- Version compatibility matrix

### SwiftUI Frameworks
- Native macOS interface components
- Charts framework for metrics
- UserNotifications for alerts
- Keychain Services for security

## Build Scripts

### Automated Building
The project includes build automation scripts for common scenarios:

```bash
# Full build with tests
./scripts/build-full.sh

# Quick development build
./scripts/build-dev.sh

# Release build with signing
./scripts/build-release.sh
```

## Testing

### Unit Tests
```bash
xcodebuild test -project DinoDB.xcodeproj -scheme DinoDB -only-testing:DinoDBTests
```

### UI Tests
```bash
xcodebuild test -project DinoDB.xcodeproj -scheme DinoDB -only-testing:DinoDBUITests
```

### Code Coverage
```bash
xcodebuild test -project DinoDB.xcodeproj -scheme DinoDB -enableCodeCoverage YES
```

## Troubleshooting

### Common Build Issues
- **SDK Version Mismatch**: Update Xcode and Swift
- **Dependency Conflicts**: Clean derived data
- **Signing Issues**: Check provisioning profiles
- **Architecture Errors**: Verify target settings

### Debug Tools
- Xcode debugger integration
- Performance profiling tools
- Memory leak detection
- Network request monitoring

### Build Optimization
- Parallel build settings
- Compiler optimization flags
- Link-time optimization
- Dead code elimination

*This is a stub - full documentation will be generated from project source*