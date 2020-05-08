from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
project_id = "lofty-door-270403"

client = automl.AutoMlClient()
# A resource that represents Google Cloud Platform location.
project_location = client.location_path(project_id, "us-central1")
response = client.list_models(project_location, "")

print("List of models:")
for model in response:
    # Display the model information.
    if (
        model.deployment_state
        == automl.enums.Model.DeploymentState.DEPLOYED
    ):
        deployment_state = "deployed"
    else:
        deployment_state = "undeployed"

    print("Model name: {}".format(model.name))
    print("Model id: {}".format(model.name.split("/")[-1]))
    print("Model display name: {}".format(model.display_name))
    print("Model create time:")
    print("\tseconds: {}".format(model.create_time.seconds))
    print("\tnanos: {}".format(model.create_time.nanos))
    print("Model deployment state: {}".format(deployment_state))