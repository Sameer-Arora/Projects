ASM = $(wildcard asm/*.asm)
HEX = $(addprefix hex/,$(notdir $(ASM:.asm=.hex)))
LOG = $(addprefix logs/,$(notdir $(HEX:.hex=.log)))

merge = logs/merge.log

default: all

all: $(LOG) $(HEX)

hex/%.hex: asm/%.asm
	@echo '.......................................................'
	 @echo 'Assembling ' $< '....'
	./assembler/bin/assembler $< $@
	@echo ' '

./assembler/bin/assembler: 

logs/%.log: hex/%.hex
	@echo 'Simulating ' $< '.....'
	./simulator/bin/sim -pipe -input $< -output $@ -mem merge.mem
	@echo ''
	@echo $@ ': file succesfulling created'
	@echo '.......................................................'



merge: $(merge)
karan: $(karan)

clean:
	rm -f $(LOG) $(HEX)
