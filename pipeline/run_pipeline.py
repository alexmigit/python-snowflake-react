from extract.extract_data import get_data
from load.load_to_snowflake import load_to_snowflake
from transform.run_transforms import run_all_transforms
from notify.slack_notify import notify_slack

# Main function to run the entire ELT pipeline
# This function orchestrates the extraction, loading, transformation, and notification processes
def main():
    try:
        notify_slack("🔁 Starting Manufacturing ELT Pipeline...")
        data = get_data()
        load_to_snowflake(data)
        run_all_transforms()
        notify_slack("✅ ELT Pipeline Completed Successfully!")
    except Exception as e:
        notify_slack(f"❌ Pipeline Failed: {str(e)}")
        raise

# Entry point for the pipeline
if __name__ == "__main__":
    main()
