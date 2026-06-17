variable "aws_region" {
  description = "AWS region where the S3 bucket will be created."
  type        = string
}

variable "bucket_name" {
  description = "Name of the S3 bucket to create. Must be globally unique."
  type        = string
}

variable "environment" {
  description = "Environment name for tagging."
  type        = string
  default     = "dev"
}

variable "project_name" {
  description = "Project name for tagging."
  type        = string
  default     = "github-actions-training"
}