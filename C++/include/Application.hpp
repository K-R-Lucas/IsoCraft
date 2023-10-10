#pragma once

class Application;

#include "Renderer.hpp"
#include "Timer.hpp"

class Application
{
public:
    Application(int _width, int _height, int _target_tps, int _target_fps);
    ~Application();

    int Run();
    void Update();
    void Tick();

    int& GetWidth();
    int& GetHeight();

private:
    int m_fps{}, m_tps, m_width, m_height;
    float m_ft{}, m_dt;
    
    Renderer* m_renderer;
    Timer m_debug_timer, m_main_timer;
};