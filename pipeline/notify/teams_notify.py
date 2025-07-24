import requests
import json
import traceback

def send_teams_notification(
    webhook_url,
    pipeline_name,
    status="Success",
    duration="N/A",
    record_count="N/A",
    logs_url="#",
    error_message=None
):
    color = "36a64f" if status.lower() == "success" else "ff0000"
    title = f"ETL Pipeline Report: **{pipeline_name}**"

    # Markdown table for metrics
    table_md = (
        f"| Status  | Duration | Records Loaded |\n"
        f"|---------|----------|----------------|\n"
        f"| {status} | {duration} | {record_count} |\n"
    )

    # Optional error details
    error_md = f"❗ **Error Details:**\n```\n{error_message}\n```" if error_message else ""

    # Construct payload
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": f"{pipeline_name} ETL Notification",
        "themeColor": color,
        "title": title,
        "sections": [
            {
                "activityTitle": f"🛠 **{pipeline_name}**",
                "activitySubtitle": "ETL Pipeline Notification",
                "text": f"📋 **Summary:**\n\n{table_md}\n\n{error_md}\n\n🔗 [View Logs]({logs_url})"
            }
        ]
    }

    try:
        response = requests.post(
            webhook_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        response.raise_for_status()
        print("✅ Teams notification sent.")
    except Exception as send_err:
        print(f"❌ Failed to send Teams notification: {send_err}")

# 👇 Example usage in ETL workflow
webhook = "https://outlook.office.com/webhook/your_webhook_url_here"

try:
    # Simulate ETL logic
    print("Running ETL...")
    # raise ValueError("Example failure")  # Uncomment to test failure
    duration = "9m 42s"
    record_count = "12,045"

    # Send success notification
    send_teams_notification(
        webhook_url=webhook,
        pipeline_name="Customer Sync",
        status="Success",
        duration=duration,
        record_count=record_count,
        logs_url="https://your-logging-service.com/jobs/customer-sync"
    )

except Exception as e:
    error_msg = traceback.format_exc()
    send_teams_notification(
        webhook_url=webhook,
        pipeline_name="Customer Sync",
        status="Failed",
        duration="N/A",
        record_count="N/A",
        logs_url="https://your-logging-service.com/jobs/customer-sync",
        error_message=error_msg
    )
    raise  # Optional: re-raise for CI/CD or logs
