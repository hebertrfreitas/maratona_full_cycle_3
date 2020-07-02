package grifts

import (
  "github.com/gobuffalo/buffalo"
	"github.com/hebertrfreitas/hello_full_cycle_golang_web/actions"
)

func init() {
  buffalo.Grifts(actions.App())
}
