variable "repository_name" {
  description = "Name of the GitHub repository to create"
  type        = string
}

variable "github_token" {
  description = "GitHub personal access token"
  type        = string
}

variable "dev_api_key" {
  description = "API key for the dev environment"
  type        = string
}

variable "prod_api_key" {
  description = "API key for the prod environment"
  type        = string
}
