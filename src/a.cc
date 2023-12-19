// Copyright 2023 hwelsters

#include <egg.h>

#include <iostream>

class Eggman : public egg::Application {
 public:
  Eggman() {}
  ~Eggman() {}
};

egg::Application* egg::CreateApplication() { return new Eggman(); }
