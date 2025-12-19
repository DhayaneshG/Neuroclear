# Neuroclear
NeuroClear is an FPGA-based adaptive noise cancellation system that uses an LMS filter to remove noise from EEG signals in real time, improving signal clarity and reliability for Brain-Computer Interface and medical applications.

## Overview
Brain-Computer Interfaces (BCIs) are transforming human interaction with technology by enabling users to control devices using neural activity. These systems play a crucial role in assistive technology,neuroprosthetics,cognitive research, and medical diagnostics. However, one of the biggest challenges in BCI development is dealing with signal contamination caused by various noise sources, such as muscle movements (EMG), eye blinks (EOG), and environmental electromagnetic interference (EMI). These unwanted signals obscure the actual brain activity, leading to reduced accuracy and reliability in BCI based applications. 

The NeuroClear project aims to tackle this challenge by developing a high-speed, real-time Adaptive Noise Canceller (ANC) implemented on an FPGA. The system employs a Least Mean Squares (LMS) adaptive filter, which continuously learns and adapts to the noise pattern, filtering it out while preserving essential neural signals. Unlike traditional filtering methods that may remove useful components along with noise, this adaptive approach dynamically distinguishes and eliminates interference based on real-time feedback. Implementing this solution on an FPGA allows for high-speed parallel processing, ultra-low latency, and real-time adaptability, making it far more efficient than software-based filtering solutions. 

The NeuroClear system is currently in the prototype development phase, with initial testing being conducted using simulated EEG datasets. The focus at this stage is on evaluating the effectiveness of the FPGA-based adaptive noise cancellation approach in improving signal clarity. Key performance metrics such as signal-to-noise ratio (SNR) enhancement, error rate reduction, and system responsiveness are being analysed to fine-tune the design. While real-time EEG testing is planned for future phases, early simulations indicate promising results in filtering out unwanted noise while preserving critical neural signals. 

This project represents a significant advancement in enhancing the robustness and accuracy of BCIs, paving the way for more reliable neurotechnology applications. The 
success of this prototype could pave the way for more accurate brain-controlled prosthetic movements, improved neurofeedback therapy, and enhanced brain signal analysis in medical and research fields.


