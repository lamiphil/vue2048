"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources
from pulumi_azure_native import web

# Create an Azure Resource Group for PreProd environment
resource_group = resources.ResourceGroup("rg-vue2048-preprod")

# Create a Static Web App in PreProd environment
stapp = web.StaticSite(
    resource_name="stapp-vue2048-preprod",
    resource_group_name=resource_group.name,
    location="West Europe",
    repository_url="",
    sku=web.SkuDescriptionArgs(name="Free", tier="Free"),
    tags=[
        ["Class", "EIT213"]
    ]
)

url = stapp.content_distribution_endpoint


