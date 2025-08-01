# Installation

## System Requirements

- **macOS**: 14.0 (Sonoma) or later
- **Architecture**: Intel or Apple Silicon (M1/M2/M3)
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 100MB free space

## Download Options

### Option 1: Direct Download (Recommended)
1. Visit [dinodb.app](https://dinodb.app)
2. Click "Download for macOS"
3. Open the downloaded DMG file
4. Drag DinoDB to your Applications folder

### Option 2: GitHub Releases
1. Go to [GitHub Releases](https://github.com/vegasq/dinodbapp/releases)
2. Download the latest `DinoDB.dmg` file
3. Follow the same installation steps as above

## First Launch

1. Open DinoDB from Applications folder
2. If you see a security warning:
   - Go to **System Settings** > **Privacy & Security**
   - Click "Open Anyway" next to the DinoDB warning
   - Confirm by clicking "Open" in the dialog

## AWS Prerequisites

Before using DinoDB, ensure you have:

### AWS Account
- Active AWS account with DynamoDB access
- IAM user or role with appropriate permissions

### Required AWS Permissions
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:ListTables",
                "dynamodb:DescribeTable",
                "dynamodb:Scan",
                "dynamodb:Query",
                "dynamodb:GetItem",
                "dynamodb:PutItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem",
                "dynamodb:CreateTable",
                "dynamodb:DeleteTable",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:ListMetrics"
            ],
            "Resource": "*"
        }
    ]
}
```

### AWS Credentials Setup

Choose one of these methods:

#### Method 1: AWS Credentials File
Create `~/.aws/credentials` with:
```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region = us-east-1

[production]
aws_access_key_id = PROD_ACCESS_KEY
aws_secret_access_key = PROD_SECRET_KEY
region = us-west-2
```

#### Method 2: DinoDB Account Storage
Add accounts directly in DinoDB (stored securely in Keychain):
1. Launch DinoDB
2. Click "Add Account"
3. Enter your AWS credentials
4. Click "Save"

## Verification

After installation:

1. Launch DinoDB
2. You should see either:
   - Your AWS profiles (if using credentials file)
   - Welcome screen to add accounts
3. Double-click an account to connect
4. Verify you can see your DynamoDB tables

## Troubleshooting

### "App can't be opened" Error
- Check that you have macOS 14.0 or later
- Try the security override steps above

### No Tables Showing
- Verify AWS credentials have correct permissions
- Check that you're in the correct AWS region
- Ensure tables exist in your AWS account

### Connection Issues
- Verify internet connectivity
- Check AWS service status
- Confirm credentials are not expired

## Next Steps

Once installed, continue to the [Quick Start Guide](quickstart.md) to begin using DinoDB.