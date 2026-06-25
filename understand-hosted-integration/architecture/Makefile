# Render WFM Integration Platform architecture diagrams.
#
# Targets:
#   make             - render everything (PlantUML + mermaid)
#   make plantuml    - render *.puml -> images/*.svg + images/*.png
#   make mermaid     - render *.mmd  -> images/*.svg + images/*.png
#   make install     - install rendering tools via brew + npm
#   make clean       - remove images/
#   make watch       - re-render on file change (needs fswatch)
#
# Tool versions tested:
#   plantuml: any recent (uses C4-PlantUML stdlib via !include URL)
#   mmdc:     @mermaid-js/mermaid-cli >= 10
#   java:     >= 11 (PlantUML needs java)

SHELL       := /bin/bash
ROOT        := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
PLANTUML_DIR := $(ROOT)/plantuml
MERMAID_DIR  := $(ROOT)/mermaid
IMAGES_DIR   := $(ROOT)/images

PUML_SOURCES := $(wildcard $(PLANTUML_DIR)/*.puml)
MMD_SOURCES  := $(wildcard $(MERMAID_DIR)/*.mmd)

PUML_SVG := $(patsubst $(PLANTUML_DIR)/%.puml,$(IMAGES_DIR)/%.svg,$(PUML_SOURCES))
PUML_PNG := $(patsubst $(PLANTUML_DIR)/%.puml,$(IMAGES_DIR)/%.png,$(PUML_SOURCES))
MMD_SVG  := $(patsubst $(MERMAID_DIR)/%.mmd,$(IMAGES_DIR)/%.svg,$(MMD_SOURCES))
MMD_PNG  := $(patsubst $(MERMAID_DIR)/%.mmd,$(IMAGES_DIR)/%.png,$(MMD_SOURCES))

.PHONY: all plantuml mermaid clean install watch help check-tools

all: plantuml mermaid
	@echo ""
	@echo "Done. Rendered to: $(IMAGES_DIR)"
	@ls -1 $(IMAGES_DIR) 2>/dev/null || true

plantuml: check-plantuml $(PUML_SVG) $(PUML_PNG)
mermaid:  check-mermaid  $(MMD_SVG) $(MMD_PNG)

$(IMAGES_DIR):
	@mkdir -p $(IMAGES_DIR)

# PlantUML -> SVG
$(IMAGES_DIR)/%.svg: $(PLANTUML_DIR)/%.puml | $(IMAGES_DIR)
	@echo "[plantuml svg] $(notdir $<)"
	@plantuml -tsvg -o $(IMAGES_DIR) $<

# PlantUML -> PNG
$(IMAGES_DIR)/%.png: $(PLANTUML_DIR)/%.puml | $(IMAGES_DIR)
	@echo "[plantuml png] $(notdir $<)"
	@plantuml -tpng -o $(IMAGES_DIR) $<

# Mermaid -> SVG
$(IMAGES_DIR)/%.svg: $(MERMAID_DIR)/%.mmd | $(IMAGES_DIR)
	@echo "[mermaid svg]  $(notdir $<)"
	@mmdc -i $< -o $@ -b transparent

# Mermaid -> PNG
$(IMAGES_DIR)/%.png: $(MERMAID_DIR)/%.mmd | $(IMAGES_DIR)
	@echo "[mermaid png]  $(notdir $<)"
	@mmdc -i $< -o $@ -b white --width 1600

check-plantuml:
	@command -v plantuml >/dev/null 2>&1 || { \
		echo "plantuml not installed. Run: make install (or: brew install plantuml)"; exit 1; }

check-mermaid:
	@command -v mmdc >/dev/null 2>&1 || { \
		echo "mmdc not installed. Run: make install (or: npm i -g @mermaid-js/mermaid-cli)"; exit 1; }

check-tools:
	@echo "java:     $$(java -version 2>&1 | head -1 || echo 'NOT FOUND')"
	@echo "plantuml: $$(plantuml -version 2>&1 | head -1 || echo 'NOT FOUND')"
	@echo "mmdc:     $$(mmdc --version 2>&1 || echo 'NOT FOUND')"

install:
	@echo "Installing PlantUML + mermaid-cli..."
	@command -v brew >/dev/null && brew install plantuml || echo "brew not found; install PlantUML manually"
	@command -v npm  >/dev/null && npm install -g @mermaid-js/mermaid-cli || echo "npm not found; install mermaid-cli manually"

clean:
	@rm -rf $(IMAGES_DIR)/*.svg $(IMAGES_DIR)/*.png
	@echo "Cleaned $(IMAGES_DIR)"

watch:
	@command -v fswatch >/dev/null 2>&1 || { \
		echo "fswatch not installed. Run: brew install fswatch"; exit 1; }
	@echo "Watching for changes..."
	@fswatch -o $(PLANTUML_DIR) $(MERMAID_DIR) | xargs -n1 -I{} $(MAKE) all

help:
	@echo "Targets:"
	@echo "  make            render all diagrams (default)"
	@echo "  make plantuml   render PlantUML only"
	@echo "  make mermaid    render mermaid only"
	@echo "  make install    install plantuml + mmdc"
	@echo "  make check-tools  show installed tool versions"
	@echo "  make watch      re-render on file change (needs fswatch)"
	@echo "  make clean      remove rendered images"
