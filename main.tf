# Configure the GitHub Provider
provider "github" {
  token = var.github_token  # Use a variable for the GitHub personal access token
}

# Create a new repository
resource "github_repository" "example_repo" {
  name        = var.repository_name
  description = "This is an example repository created by Terraform"

  visibility = "private"  # or "public" if you want it to be public
  
  has_issues    = true
  has_wiki      = true
  has_downloads = true

  allow_merge_commit = true
  allow_squash_merge = true
  allow_rebase_merge = true

  auto_init = true  # Initialize with a README
}

# Create a development environment
resource "github_repository_environment" "dev" {
  repository  = github_repository.example_repo.name
  environment = "dev"
  
  deployment_branch_policy {
    protected_branches     = false
    custom_branch_policies = true
  }
}

# Create a production environment
resource "github_repository_environment" "prod" {
  repository  = github_repository.example_repo.name
  environment = "prod"
  
  deployment_branch_policy {
    protected_branches     = true
    custom_branch_policies = false
  }
}

# # Add a secret to the dev environment
# resource "github_actions_environment_secret" "dev_secret" {
#   repository      = github_repository.example_repo.name
#   environment     = github_repository_environment.dev.environment
#   secret_name     = "DEV_API_KEY"
#   plaintext_value = var.dev_api_key  # Use a variable for the secret value
# }
# 
# # Add a secret to the prod environment
# resource "github_actions_environment_secret" "prod_secret" {
#   repository      = github_repository.example_repo.name
#   environment     = github_repository_environment.prod.environment
#   secret_name     = "PROD_API_KEY"
#   plaintext_value = var.prod_api_key  # Use a variable for the secret value
# }

# Output the repository URL
output "repository_url" {
  value = github_repository.example_repo.html_url
}
