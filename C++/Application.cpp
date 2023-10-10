#include "Application.hpp"
#include "GLFW/glfw3.h"
#include <iostream>

Application::Application(int _width, int _height, int _target_tps, int _target_fps):
    m_tps(_target_tps), m_width(_width), m_height(_height), m_dt(1.0f/static_cast<float>(_target_fps)), m_debug_timer(4), m_main_timer(60)
{
    m_renderer = new Renderer{this};
}

Application::~Application()
{

}

int Application::Run()
{
    GLFWwindow* window = m_renderer->GetWindow();

    while (!glfwWindowShouldClose(window)) {
        glfwPollEvents();

        // Drawing
        glClear(GL_COLOR_BUFFER_BIT);

        glfwSwapBuffers(window);

        // Updating
        m_main_timer.Accumulate(m_ft);
        m_debug_timer.Accumulate(m_ft);

        // Sync - main loop
        while (m_main_timer.Tick())
        {

        }

        // Sync - debug/logging
        while (m_debug_timer.Tick())
        {
            std::cout << 1.0f/m_ft << "\n";
        }
    }

    glfwTerminate();
    return 0;
}

int& Application::GetWidth()
{
    return m_width;
}

int& Application::GetHeight()
{
    return m_height;
}