import { writable } from "svelte/store";
import type { Writable } from "svelte/store";

export type ScrollStatus = "top" | "down" | "up" | "none";
interface ScrollStatusEntry {
  status: ScrollStatus,
  lastChange: number,
}
type ScrollStatusRecord = Record<number, ScrollStatusEntry>;

const defaultOffset = 60;
const defaultEntry: ScrollStatusEntry = {
  status: "none",
  lastChange: 0,
}
const defaultRecord: ScrollStatusRecord = {};
defaultRecord[defaultOffset] = defaultEntry;

const { subscribe, update }: Writable<ScrollStatusRecord> = writable(defaultRecord);

function setStatus(offset: number, value: ScrollStatus) {
  /// private, set the current status for a given offset
  update(rec => {
    rec[offset]["status"] = value;
    return rec;
  })
}

function setEntry(offset: number, value: ScrollStatusEntry) {
  /// private, set or add an entry for a given offset
  update(rec => {
    rec[offset] = value;
    return rec;
  })
}

function get(offset: number = defaultOffset) {
  /// public, get the status for a given offset or default
  let value: ScrollStatus;
  update(rec => {
    if (offset in rec) {
      value = rec[offset]["status"];
      return rec;
    } else {
      value = compute(offset);
      return rec;
    }
  });
  return value!;
}

function compute(offset: number | null | "all" = "all"): ScrollStatus {
  /// if offset is "all", re-compute the status for every offset in the record
  /// if offset is null, compute the status for the default offset
  /// if offset is a number, compute the status for the given offset

  let returnValue: ScrollStatus;
  update(rec => {
    if (offset === "all") {
      let defaultValue: ScrollStatus;
      for (let i in rec!) {
        compute(i);
      }
      defaultValue = get(defaultOffset);

      returnValue = defaultValue!;
      return rec;
    }

    if (offset === null) {
      offset = defaultOffset;
    }
    const scroll = window.pageYOffset;
    if (! (offset in rec!)) {
      rec[offset] = defaultEntry;
    }

    if (scroll <= offset) {
      setStatus(offset, "top");
      returnValue = "top";
    } else if (rec[offset]["lastChange"] - scroll - offset > 0) {
      rec[offset]["lastChange"] = scroll;
      setStatus(offset, "up");
      returnValue = "up";
    } else if (scroll - rec[offset]["lastChange"] - offset > 0) {
      rec[offset]["lastChange"] = scroll;
      setStatus(offset, "down");
      returnValue = "down";
    } else {
      setStatus(offset, "none");
      returnValue = "none";
    }

    // if (returnValue !== "none") console.log(offset, returnValue);

    return rec;
  });
  return returnValue!;
}

export const scroll_status = {
  subscribe,
  compute,
  get,
}
