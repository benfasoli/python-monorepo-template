module "api" {
  source = "./modules/auth"
}

module "users" {
  source = "./modules/auth"
}
