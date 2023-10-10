#include "Renderer.hpp"

Renderer::Renderer(Application& _app): m_app(_app)
{
    glfwInit();
    m_window = glfwCreateWindow(m_app.GetWidth(), m_app.GetHeight(), "IsoCraft++", NULL, NULL);
    glfwMakeContextCurrent(m_window);

}

GLFWwindow* Renderer::GetWindow()
{
    return m_window;
}