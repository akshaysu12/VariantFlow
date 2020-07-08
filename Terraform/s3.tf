resource "aws_s3_bucket" "pipelines_bucket" {
  bucket = "variantflow-bucket"
  acl    = "private"

  tags = {
    Name        = "VariantFlow"
    Environment = "Testing"
  }
}