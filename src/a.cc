// Copyright 2023 hwelsters

#include <egg.h>

#include <iostream>

class Eggman : public egg::Application {
 public:
  Eggman() {
    std::cout << "binks";
  }
  ~Eggman() {}
};

egg::Application* egg::CreateApplication() { return new Eggman(); }
