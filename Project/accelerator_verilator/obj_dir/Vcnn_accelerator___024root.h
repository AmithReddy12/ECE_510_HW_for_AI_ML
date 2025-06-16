// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See Vcnn_accelerator.h for the primary calling header

#ifndef VERILATED_VCNN_ACCELERATOR___024ROOT_H_
#define VERILATED_VCNN_ACCELERATOR___024ROOT_H_  // guard

#include "verilated.h"


class Vcnn_accelerator__Syms;

class alignas(VL_CACHE_LINE_BYTES) Vcnn_accelerator___024root final : public VerilatedModule {
  public:

    // DESIGN SPECIFIC STATE
    VL_IN8(clk,0,0);
    VL_IN8(rst,0,0);
    VL_IN8(valid_in,0,0);
    VL_IN8(pixel_in,7,0);
    VL_OUT8(emotion_out,2,0);
    VL_OUT8(valid_out,0,0);
    CData/*0:0*/ __Vtrigprevexpr___TOP__clk__0;
    CData/*0:0*/ __Vtrigprevexpr___TOP__rst__0;
    CData/*0:0*/ __VactContinue;
    IData/*31:0*/ __VactIterCount;
    VlTriggerVec<2> __VactTriggered;
    VlTriggerVec<2> __VnbaTriggered;

    // INTERNAL VARIABLES
    Vcnn_accelerator__Syms* const vlSymsp;

    // CONSTRUCTORS
    Vcnn_accelerator___024root(Vcnn_accelerator__Syms* symsp, const char* v__name);
    ~Vcnn_accelerator___024root();
    VL_UNCOPYABLE(Vcnn_accelerator___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
};


#endif  // guard
