# Overview

DinoDB is a native macOS application designed to make working with AWS DynamoDB tables intuitive and efficient. Whether you're a developer, DevOps engineer, or data analyst, DinoDB provides the tools you need to manage your DynamoDB infrastructure.

## Why DinoDB?

### Native macOS Experience
Built specifically for macOS using SwiftUI, DinoDB feels at home on your Mac with:
- Native look and feel following macOS Human Interface Guidelines
- System integration with Keychain for secure credential storage
- Responsive design that adapts to your workspace

### Enterprise-Ready Security
- Secure credential storage in macOS Keychain
- Support for AWS credentials file integration
- No credentials ever logged or stored in plain text
- Multiple account management with visual distinction

### Real-Time Monitoring
- CloudWatch integration for performance metrics
- Interactive charts with multiple time ranges
- Configurable metric alerts with system notifications
- Trend analysis and capacity monitoring

### Developer-Friendly
- Comprehensive debug logging system
- JSON syntax highlighting
- Query builder with visual interface
- Multiple view modes (Table and JSON)

## Architecture

DinoDB is built using modern Swift technologies:

- **SwiftUI**: Declarative UI framework for native macOS interface
- **SwiftData**: Model persistence and account management
- **AWS SDK for Swift**: Official AWS integration
- **Charts Framework**: Native metric visualization
- **Keychain Services**: Secure credential storage

## Target Users

- **Developers**: Debug and test DynamoDB applications
- **DevOps Engineers**: Monitor table performance and capacity
- **Data Analysts**: Query and analyze DynamoDB data
- **System Administrators**: Manage multiple AWS accounts and regions