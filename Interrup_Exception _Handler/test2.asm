.text 
	B .main 
	B .excep_handler 
	B .int_handler 
 
.main: 
	add r0,r0,4
	add r0,r0,4
	add r0,r0,4
	cmp r0,4
	mov r0,33000
	ld r1,[r0]
	st r6,[r0]
	bgt .exit
	B .exit

.excep_handler:  

	movz oldSP,sp
	mov sp, 32150   //stack of size 100000 for interupt

	// update the stack pointer 
	sub sp, sp, 72

	//spill all the registers other than sp
	st r0, 0[sp]
	st r1, 4[sp]
	st r2, 8[sp]
	st r3, 12[sp]
	st r4, 16[sp]
	st r5, 20[sp]       
	st r6, 24[sp]        
	st r7, 28[sp]
	st r8, 32[sp]
	st r9, 36[sp]
	st r10, 40[sp]
	st r11, 44[sp]
	st r12, 48[sp]
	st r13, 52[sp]
	st r15, 56[sp]
	
	//save the stack pointer 
	movz r0, oldSP
	st r0, 60[sp]

	//save the flags register 
	movz r0,oldFlags
	st r0, 64[sp]

	// save the oldPC
	movz r0, oldPC
	st r0, 68[sp]

	// code of the interrupt handler

	// restore all the registers other than sp
	ld r0, 0[sp]
	ld r1, 4[sp]
	ld r2, 8[sp]
	ld r3, 12[sp]
	ld r4, 16[sp]
	ld r5, 20[sp]       
	ld r6, 24[sp]        
	ld r7, 28[sp]
	ld r8, 32[sp]
	ld r9, 36[sp]
	ld r10, 40[sp]
	ld r11, 44[sp]
	ld r12, 48[sp]
	ld r13, 52[sp]
	ld r15, 56[sp]
	
	// restore the oldPC register 
	ld r0, 68[sp]
	movz oldPC, r0

	// restore the flags register 
	ld r0, 64[sp]
	movz oldflags, r0

	//restore the stack pointer 
	movz r0, oldSP
	ld r0, 60[sp]

	// restore the stack pointer 
	movz sp, oldSP
	
	
	// restore the stack pointer 
	movz sp, oldSP
	
	// update the stack pointer 
	add sp, sp, 72

	// return to the program 
	retz 

.int_handler:

	movz oldSP,sp
	mov sp, 0x7fff   //stack of size 100000 for interupt

	// update the stack pointer 
	sub sp, sp, 72

	//spill all the registers other than sp
	st r0, 0[sp]
	st r1, 4[sp]
	st r2, 8[sp]
	st r3, 12[sp]
	st r4, 16[sp]
	st r5, 20[sp]       
	st r6, 24[sp]        
	st r7, 28[sp]
	st r8, 32[sp]
	st r9, 36[sp]
	st r10, 40[sp]
	st r11, 44[sp]
	st r12, 48[sp]
	st r13, 52[sp]
	st r15, 56[sp]
	
	//save the stack pointer 
	movz r0, oldSP
	st r0, 60[sp]

	//save the flags register 
	movz r0,oldFlags
	st r0, 64[sp]

	// save the oldPC
	movz r0, oldPC
	st r0, 68[sp]

	// code of the interrupt handler
	
	// restore the oldPC register 
	ld r0, 68[sp]
	movz oldPC, r0

	// restore the flags register 
	ld r0, 64[sp]
	movz oldflags, r0

	//restore the stack pointer 
	ld r0, 60[sp]
	movz  oldSP,r0

	// restore all the registers other than sp
	ld r0, 0[sp]
	ld r1, 4[sp]
	ld r2, 8[sp]
	ld r3, 12[sp]
	ld r4, 16[sp]
	ld r5, 20[sp]       
	ld r6, 24[sp]        
	ld r7, 28[sp]
	ld r8, 32[sp]
	ld r9, 36[sp]
	ld r10, 40[sp]
	ld r11, 44[sp]
	ld r12, 48[sp]
	ld r13, 52[sp]
	ld r15, 56[sp]


	// update the stack pointer 
	add sp, sp, 72

	// restore the stack pointer 
	movz sp, oldSP
	
	// return to the program 
	retz 
	
.exit:

.end  
	