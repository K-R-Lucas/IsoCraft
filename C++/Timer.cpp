#include "Timer.hpp"


Timer::Timer() {}
Timer::Timer(int _tps): m_tps(_tps), m_dt(1.0f/static_cast<float>(_tps)) {}

void Timer::Accumulate(float& _ft)
{
    m_ft = _ft;
    m_t += _ft;
}

bool Timer::Tick()
{
    bool c = m_t >= m_ft;

    if (c) {
        m_t -= m_dt;
        return true;
    }

    return false;
}