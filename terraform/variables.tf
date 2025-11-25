variable "aws_region" {
  default = "us-east-1"
}

variable "ami" {
  default = "ami-04b70fa74e45c3917"
}

variable "instance_type" {
  default = "t3.small"
}

variable "key_name" {
  default = "gabrielm-newkeypair"
}

variable "vpc_id" {
  default = "vpc-06786ee7f7a163059"
}

variable "subnet_id" {
  default = "subnet-044f002f78f0c4f30"
}
