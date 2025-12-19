# Neuroclear
NeuroClear is an FPGA-based adaptive noise cancellation system that uses an LMS filter to remove noise from EEG signals in real time, improving signal clarity and reliability for Brain-Computer Interface and medical applications.

## Tech stack
[![My Skills](https://skillicons.dev/icons?i=python,matlab,c,raspberrypi,vscode&theme=light)](https://skillicons.dev)


## Overview
Brain-Computer Interfaces (BCIs) are transforming human interaction with technology by enabling users to control devices using neural activity. These systems play a crucial role in assistive technology,neuroprosthetics,cognitive research, and medical diagnostics. However, one of the biggest challenges in BCI development is dealing with signal contamination caused by various noise sources, such as muscle movements (EMG), eye blinks (EOG), and environmental electromagnetic interference (EMI). These unwanted signals obscure the actual brain activity, leading to reduced accuracy and reliability in BCI based applications. 

The NeuroClear project aims to tackle this challenge by developing a high-speed, real-time Adaptive Noise Canceller (ANC) implemented on an FPGA. The system employs a Least Mean Squares (LMS) adaptive filter, which continuously learns and adapts to the noise pattern, filtering it out while preserving essential neural signals. Unlike traditional filtering methods that may remove useful components along with noise, this adaptive approach dynamically distinguishes and eliminates interference based on real-time feedback. Implementing this solution on an FPGA allows for high-speed parallel processing, ultra-low latency, and real-time adaptability, making it far more efficient than software-based filtering solutions. 

The NeuroClear system is currently in the prototype development phase, with initial testing being conducted using simulated EEG datasets. The focus at this stage is on evaluating the effectiveness of the FPGA-based adaptive noise cancellation approach in improving signal clarity. Key performance metrics such as signal-to-noise ratio (SNR) enhancement, error rate reduction, and system responsiveness are being analysed to fine-tune the design. While real-time EEG testing is planned for future phases, early simulations indicate promising results in filtering out unwanted noise while preserving critical neural signals. 

This project represents a significant advancement in enhancing the robustness and accuracy of BCIs, paving the way for more reliable neurotechnology applications. The 
success of this prototype could pave the way for more accurate brain-controlled prosthetic movements, improved neurofeedback therapy, and enhanced brain signal analysis in medical and research fields.

## LMS Algorithm Overview
### Mathematical Representation:
- Weight update equation: <img width="320" height="80" alt="image" src="https://github.com/user-attachments/assets/ad42f2d4-2517-44ae-9824-bb2adb58f0f9" />
- Error computation: <img width="256" height="25" alt="image" src="https://github.com/user-attachments/assets/b30d7150-3cb6-4c04-b25b-0915a8487df3" />
- Adaptive nature: Self-adjusting filter coefficients
### Key Parameters:
- Step size (µ): Controls adaptation speed and stability
- Input signal (X(n)): Incoming EEG signal
- Desired response (d(n)): Clean EEG signal reference

## Overall Process
<img width="628" height="456" alt="image" src="https://github.com/user-attachments/assets/73de612a-71ae-4d2e-acb8-bccaf83fa760" />

## Simulation and Testing
### - MATLAB for Algorithm Validation:
- Simulating EEG noise removal
- Evaluating filter convergence and artifact reduction
### - HDL Test benches for FPGA Verification
### - Performance Metrics:
- Signal-to-noise ratio (SNR) improvement
- Convergence speed
- Mean squared error reduction

### Case 1:
Fast noise reduction but with possible instability
<table>
  <tr>
    <td align="center" width="33%">
        <img width="406" height="304" alt="image" src="https://github.com/user-attachments/assets/a5485359-5c68-4488-a010-8da7ef516da3" />
      <b>Output</b><br/>
    </td>
      <td align="center" width="33%">
        <img width="403" height="300" alt="image" src="https://github.com/user-attachments/assets/81fa9953-719e-4ebd-9fd3-caad0e6f31fb" />
      <b>MSE Reduction</b><br/>
    </td>
      <td align="center" width="33%">
       <img width="401" height="300" alt="image" src="https://github.com/user-attachments/assets/8810a381-d0eb-40ce-b0a5-cc0139915954" />
      <b>Convergence Speed</b><br/>
    </td>
  </tr>
</table>
<b>Observation:</b>
Fast noise reduction with rapid SNR improvement due to a high step size (μ=0.05\mu = 0.05μ=0.05), but may cause slight oscillations. Converges quickly with potential instability in weight updates.


### Case 2:
Stable noise reduction but slow learning
<table>
  <tr>
    <td align="center" width="33%">
        <img width="428" height="322" alt="image" src="https://github.com/user-attachments/assets/a4e15a4c-fbf7-4cf6-8b88-b001e0ea777c" />
      <b>Output</b><br/>
    </td>
      <td align="center" width="33%">
        <img width="421" height="316" alt="image" src="https://github.com/user-attachments/assets/e490b270-dd6e-4872-b788-d7b487a511ec" />
      <b>MSE Reduction</b><br/>
    </td>
      <td align="center" width="33%">
       <img width="423" height="316" alt="image" src="https://github.com/user-attachments/assets/ab465474-df6c-4a2e-b5a3-b8e99a1f9ece" />
      <b>Convergence Speed</b><br/>
    </td>
  </tr>
</table>
<b>Observation:</b>
Stable noise reduction with gradual SNR improvement due to a low step size (μ=0.005\mu = 0.005μ=0.005), ensuring smooth adaptation. Converges slowly but minimizes oscillations and instability.

