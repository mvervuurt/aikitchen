from pprint import pprint
from promptflow.client import PFClient, load_run
from multiprocessing import freeze_support

def main():
    # Initialize client
    pf = PFClient()

    # load a run from YAML file
    base_run = load_run(
        source="code/promptflow/pf_first/run.yaml",
    )

    # create the run
    run_output = pf.runs.create_or_update(run=base_run)
    details = pf.get_details(run_output)
    pprint(details.head())

if __name__ == '__main__':
    freeze_support()
    main()