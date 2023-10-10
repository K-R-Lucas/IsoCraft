#pragma once

class Timer
{
public:
    Timer();
    Timer(int _tps);

    void Accumulate(float& _ft);
    bool Tick();

private:
    float m_dt{}, m_t{}, m_ft{};
    int m_tps;
};