# Every Action

Every kind of action Workspace runs, one section each. Every value says when it last ran, so it's clear whether its action ran. An action that's stopped leaves its last value in the file: a kept value is part of the document.

## When the document opens

Runs once each time the document opens. Needs nothing, so nothing is asked.

Opened: <!--[kept demo/opened]-->not run yet<!--[/kept]-->

Budget: <!--[kept demo/total {:items [14400 4863 920]}]-->not run yet<!--[/kept]-->

Count: <!--[kept demo/count {:items [3 1 4 1 5 9 2 6]}]-->not run yet<!--[/kept]-->

## Kept for a while

`:fresh "PT2M"`: runs on opening only when its value is more than two minutes old. Open, close and reopen within two minutes: the time doesn't change.

Fresh: <!--[kept demo/fresh]-->not run yet<!--[/kept]-->

## From the web, once allowed

Asks first: one action, used in three places, each with its own input. Until it's allowed, each value shows what it last kept.

Dublin: <!--[kept demo/place {:q "Dublin"}]-->not looked up yet<!--[/kept]-->

Lisbon: <!--[kept demo/place {:q "Lisbon"}]-->not looked up yet<!--[/kept]-->

Kyoto: <!--[kept demo/place {:q "Kyoto"}]-->not looked up yet<!--[/kept]-->

## When you tap it

`:on :tap`: runs only when its value is tapped while reading.

Tapped: <!--[kept demo/tapped]-->tap me<!--[/kept]-->

## On a clock

Runs while the document is open, when its time comes. A plain cron string, a cron map, and a single moment.

Every minute: <!--[kept demo/minute]-->not run yet<!--[/kept]-->

Every five minutes: <!--[kept demo/five]-->not run yet<!--[/kept]-->

Once, at midnight on 1 Jan 2027 in London: <!--[kept demo/once]-->waiting for 1 Jan 2027<!--[/kept]-->

## When another file changes

Reads a file beside this one, and runs again when it changes. Asks first. Edit `Packing.txt` or `Budget.table` and come back.

Packing list: <!--[kept demo/packing]-->not read yet<!--[/kept]-->

Budget table: <!--[kept demo/budget]-->not read yet<!--[/kept]-->

Canvas: <!--[kept demo/canvas]-->not read yet<!--[/kept]-->

## Live, not saved

`{:show …}`: drawn on this device only, never written into the file. The file keeps what's between the markers; Workspace shows the live value over it.

Now: <!--[kept demo/live]-->shown live in Workspace<!--[/kept]-->

Both: <!--[kept demo/both]-->kept, and shown live<!--[/kept]-->

## What fails, and how

Each of these fails on purpose. Its value stays as it was, marked stale, and the reason is reported.

An expired certificate (error): <!--[kept demo/expired]-->not fetched yet<!--[/kept]-->

A host it didn't declare (refused): <!--[kept demo/undeclared]-->not fetched yet<!--[/kept]-->

A misspelt function (failed, with a suggestion): <!--[kept demo/typo {:items [1 2 3]}]-->not run yet<!--[/kept]-->

Too much work (limit or timeout): <!--[kept demo/forever]-->not run yet<!--[/kept]-->

Where this device is (denied: not answered yet): <!--[kept demo/where]-->not located yet<!--[/kept]-->

A question for you (denied: not answered yet): <!--[kept demo/ask]-->not asked yet<!--[/kept]-->

## Never run: written about, in code

A marker or an action inside code is text about actions, so it shows as written and nothing runs:

```markdown
Total: <!--[kept demo/total {:items [1 2]}]-->?<!--[/kept]-->
```

And inline: `<!--[kept demo/opened]-->not run<!--[/kept]-->`.

<!--action
{:id :demo/opened :on :open
 :fn (fn [_ env ctx] {:keep (str "ran at " (env/now))})}
-->

<!--action
{:id :demo/total :on :open
 :fn (fn [{:keys [items]} env ctx]
       {:keep (str (env/format :currency (sum items)) " across " (count items) " · ran at " (env/now))})}
-->

<!--action
{:id :demo/count :on :open
 :fn (fn [{:keys [items]} env ctx]
       {:keep (str (env/format :number (sum items)) " from " (count items) " numbers · ran at " (env/now))})}
-->

<!--action
{:id :demo/fresh :on :open :fresh "PT2M"
 :fn (fn [_ env ctx] {:keep (str "ran at " (env/now))})}
-->

<!--action
{:id :demo/place :on :open
 :needs {:fetch ["nominatim.openstreetmap.org"]}
 :fn (fn [{:keys [q]} env ctx]
       (let [r (first (env/fetch "https://nominatim.openstreetmap.org/search" {:q q :format "json" :limit 1}))]
         {:keep (str (get r :lat) ", " (get r :lon) " · fetched at " (env/now))}))}
-->

<!--action
{:id :demo/tapped :on :tap
 :fn (fn [_ env ctx] {:keep (str "tapped at " (env/now))})}
-->

<!--action
{:id :demo/minute :on [:cron "* * * * *"]
 :fn (fn [_ env ctx] {:keep (str "ticked at " (env/now))})}
-->

<!--action
{:id :demo/five :on [:cron {:minute "*/5"} :tz "Europe/London"]
 :fn (fn [_ env ctx] {:keep (str "ticked at " (env/now))})}
-->

<!--action
{:id :demo/once :on [:at "2027-01-01T00:00:00+00:00[Europe/London]"]
 :fn (fn [_ env ctx] {:keep (str "rang at " (env/now))})}
-->

<!--action
{:id :demo/packing :on [:change "Packing.txt"]
 :needs {:read ["Packing.txt"]}
 :fn (fn [_ env ctx] {:keep (str (env/read "Packing.txt") " · read at " (env/now))})}
-->

<!--action
{:id :demo/budget :on [:change "Budget.table"]
 :needs {:read ["Budget.table"]}
 :fn (fn [_ env ctx]
       (let [t (env/read "Budget.table")]
         {:keep (str (env/format :currency (sum (map (fn [r] (get r :amount)) (get t :rows)))) " in " (count (get t :rows)) " rows · read at " (env/now))}))}
-->

<!--action
{:id :demo/canvas :on [:change "Every Action.canvas"]
 :needs {:read ["Every Action.canvas"]}
 :fn (fn [_ env ctx] {:keep (str (count (get (env/read "Every Action.canvas") :nodes)) " nodes · read at " (env/now))})}
-->

<!--action
{:id :demo/live :on [:cron "* * * * *"]
 :fn (fn [_ env ctx] {:show (str "live at " (env/now))})}
-->

<!--action
{:id :demo/both :on :open
 :fn (fn [_ env ctx] {:keep (str "kept at " (env/now)) :show (str "shown at " (env/now))})}
-->

<!--action
{:id :demo/expired :on :open
 :needs {:fetch ["expired.badssl.com"]}
 :fn (fn [_ env ctx] {:keep (str (env/fetch "https://expired.badssl.com/") " · fetched at " (env/now))})}
-->

<!--action
{:id :demo/undeclared :on :open
 :needs {:fetch ["example.org"]}
 :fn (fn [_ env ctx] {:keep (str (env/fetch "https://example.com/") " · fetched at " (env/now))})}
-->

<!--action
{:id :demo/typo :on :open
 :fn (fn [{:keys [items]} env ctx] {:keep (str (cuont items) " items")})}
-->

<!--action
{:id :demo/forever :on :open
 :fn (fn [_ env ctx] {:keep (str (reduce + (range 100000000)))})}
-->

<!--action
{:id :demo/where :on :open
 :needs {:locate true}
 :fn (fn [_ env ctx] {:keep (str (env/locate) " · located at " (env/now))})}
-->

<!--action
{:id :demo/ask :on :open
 :needs {:ask true}
 :fn (fn [_ env ctx] {:keep (str (env/ask "Which colour?" ["red" "green"]) " · answered at " (env/now))})}
-->
