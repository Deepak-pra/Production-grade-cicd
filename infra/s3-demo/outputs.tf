output "bucket_name" {
  description = "Created S3 bucket name."
  value       = aws_s3_bucket.demo.bucket
}

output "bucket_arn" {
  description = "Created S3 bucket ARN."
  value       = aws_s3_bucket.demo.arn
}

output "bucket_region" {
  description = "AWS region used for this bucket."
  value       = var.aws_region
}

output "public_access_block_enabled" {
  description = "Indicates that S3 public access block is configured."
  value       = true
}

output "versioning_enabled" {
  description = "Indicates that S3 bucket versioning is enabled."
  value       = true
}

output "encryption_enabled" {
  description = "Indicates that SSE-S3 encryption is enabled."
  value       = true
}