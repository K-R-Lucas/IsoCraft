#pragma once

class Renderer;

#include "GLFW/glfw3.h"
#include "Application.hpp"

class Renderer
{
public:
    Renderer(Application* _app);
    GLFWwindow* GetWindow();

private:
    GLFWwindow* m_window;
    Application* m_app;
};